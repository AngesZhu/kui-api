from datetime import datetime
from setting.schedule.job_info_schema import JobInfo
from setting.schedule.schedule_cli_utils import schedule


def scheduleAdd(job_info, request_task):
    """
    apscheduler 操作封装
    https://apscheduler.readthedocs.io/en/master/?badge=latest
    :param job_info: 任务信息
    :param request_task: 执行的函数
    :return: 返回执行结果
    """
    res = schedule.get_job(job_id=job_info.id)
    if res:
        return "该任务-{}-已在调度中心，不可重复添加".format(job_info.id)

    job_params = {
        "id": str(job_info.id),
        "type": job_info.type,
        "method": job_info.method,
        "path": job_info.path,
        "param": job_info.param,
        "headers": job_info.headers,
    }

    try:
        cron_obj = eval(job_info.corn)
    except:
        cron_obj = str(job_info.corn).split(':')

    _exe_data = {
        "func": request_task,
        "trigger": job_info.type,
        "id": str(job_info.id),
        "next_run_time": datetime.now(),
        "kwargs": {"job_info": job_params, },
    }

    if isinstance(cron_obj, dict):
        if job_info.type == "interval":
            if cron_obj["type"] == "hour":
                _exe_data["hours"] = cron_obj["corn"]
            elif cron_obj["type"] == "minute":
                _exe_data["minutes"] = cron_obj["corn"]
            elif cron_obj["type"] == "second":
                _exe_data["seconds"] = cron_obj["corn"]

        elif job_info.type == "cron":
            _temp = str(cron_obj["time"]).split(":")
            _exe_data["hour"] = _temp[0]
            _exe_data["minute"] = _temp[1]
            _exe_data["second"] = _temp[2]
            if cron_obj["type"] == "week":
                _exe_data["day_of_week"] = ','.join(cron_obj["corn"])
            elif cron_obj["type"] == "day":
                _exe_data["day"] = ','.join(cron_obj["corn"])

            else:
                return "执行时间配置异常"
        else:
            return "任务类型异常"
    else:
        new_cron = [int(cron) for cron in cron_obj]
        _exe_data["run_date"] = datetime(*new_cron)

    schedule_job = schedule.add_job(**_exe_data)
    return "任务添加成功,任务id-{}".format(schedule_job.id)


def execute_add(job_info: JobInfo, request_task):
    job_info.id = str(job_info.id)
    job = schedule.get_job(job_info.id)
    if job:
        return f"任务-{job.id}-已在调度中心,请移除在执行!"
    schedule_job = schedule.add_job(func=request_task, kwargs={"job_info": job_info.dict()}, run_date=datetime.now(),
                                    trigger='date', id=str(job_info.id))
    return "任务运行成功-{}".format(schedule_job.id)
