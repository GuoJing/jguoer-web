<%!
    from lib.consts import user_info, active_users, admin_users
%>
<%inherit file="/base.mako"/>
<%namespace name="utils" file="/widgets/banner.mako" />

<%def name="main()">
${utils.banner(user.name)}
<div class="admin_content">
%if user.pic_url=='None':
<img src="/images/none-avatar.png" class="avatar" align="left"/>
%else:
<img src="${user.pic_url}" class="avatar" align="left"/>
%endif
</div>
${user.nickname}的个人主页<br/>
%if user.name in admin_users:
你是激活的<b>管理员</b>
%else:
你是激活的<b>用户</b>
%endif
%if user.name in admin_users:
<br/>
<div class="manage">
    <div class="title">
        <h2>所有用户</h2>
    </div>
    <div class="content">
        %for oneuser in user_info:
            ${oneuser}
        %endfor
    </div>
</div>
<div class="manage">
    <div class="title">
        <h2>激活用户</h2>
    </div>
    <div class="content">
        %for oneuser in active_users:
            ${oneuser}
        %endfor
    </div>
</div>
<div class="manage">
    <div class="title">
        <h2>管理员用户</h2>
    </div>
    <div class="content">
        %for oneuser in admin_users:
            ${oneuser}
        %endfor
    </div>
</div>
%endif
</%def>
