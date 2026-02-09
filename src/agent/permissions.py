def check_tool_permission(tool_name, allowed_tools):
    if tool_name not in allowed_tools:
        raise PermissionError("Tool not allowed")
