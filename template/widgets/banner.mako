<%!
    from lib.consts import user_info, active_users, admin_users
%>
<%def name="banner(name)">
<div class="admin_banner">                                                                
<a href="/admin/main">我</a>                                                         
%if name in admin_users:
<a href="/admin/add">添加</a>                                                      
<a href="/admin/manage">管理</a>                                                   
%endif
<a href="/admin/logout">退出</a>                                                   
</div>  
</%def>
