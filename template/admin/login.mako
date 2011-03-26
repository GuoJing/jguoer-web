<%inherit file="/base.mako"/>

<%def name="main()">
<form id="loginform" action="/admin" method="post">
<table>
<tr>
    <td>用户名:</td>
    <td>
        <input id="name" type="text" name="name"/><br/>
    </td>
</tr>
<tr>
    <td>密码:</td>
    <td>
        <input id="pwd" type="password" name="pwd"/>
    </td>
</tr>
</table>
<input type="submit" value="登录"/>
<span class="error">${error or ''}</span>
</form>
</%def>

<%def name="css()">
table {width:30%}
</%def>
