def build_task_fail_message(
    priority: int = 3, num_errors_7: int = 0, num_errors_30: int = 0, **context
) -> str:
    """Builds alert message on DAG task failure"""
    priority_emoji = {1: "🔴", 2: "🟡", 3: "🟢"}
    emoji = priority_emoji[
        min(
            context["dag"].params.get("dag_alert_priority", 3),
            context["task_instance"].task.params.get("task_alert_priority", 3),
            priority,
        )
    ]

    data_row = (
        f"DAG:      {context['task_instance'].dag_id}\n"
        f"Task:     {context['task_instance'].task_id}\n"
        f"Start:    {context['logical_date'].strftime('%Y-%m-%d %H:%M:%S')}+0\n"
        f"Errors:   {num_errors_7}w/{num_errors_30}m"
    )

    message = f"{emoji} *Task Failure* → [Log]({'127.0.0.1'})\n"
    message += f"```\n{data_row}\n```"
    return message
