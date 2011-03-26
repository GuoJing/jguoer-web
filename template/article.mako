<%!
    from lib.utils import replace_html
    from lib.consts import user_info
%>
<%inherit file="/base.mako"/>
<%def name="main()">
%if not article:
    好像并没有这个文章
%else:
    <div class="item">
        <%
            time = article.time
            title = article.title
            content = article.content.replace('\n\n', '\n').replace('\n',"<br/>")
            name = article.author
            info = user_info[name].split(',')
            nickname = info[0]
            pic = info[1]
        %>
        <h1>${title}</h1>
        <div class="admin">${time}</div>
        <div class="content">
        %if pic=='None':
        <img src="/images/none-avatar.png" title="${nickname}" class="avatar" align="right"/>
        %else:
        <img src="${pic}" class="avatar" align="right" title="${nickname}"/>
        %endif
        ${content or '这篇文章没有正文'|n, str}
        </div>
    </div>
    <div class="reply"></div>
    <!--
    <div class="show_reply"><span>添加评论</span></div>
    <div class="reply_form">
    <h2>添加评论</h2> 
        <table>
            <tr>
                <td width="30px">昵称</td>
                <td><input name="name" value="匿名用户" class="input"/></td>
            </tr>
            <tr>
                <td width="30px">网址</td>
                <td><input name="url" value="" class="input"/></td>
            </tr>
            <tr>
                <td colspan="2">内容</td>
            </tr>
            <tr>
                <td colspan="2">
                    <textarea class="textarea" name="content"></textarea>
                </td>
            </tr>
        </table>
        <input type="submit" value="评论这篇文章" disabled="true" id="reply"/>
        <span class="error">你的IP暂时还无法评论</span>
    </div>
    -->
%endif
</%def>

<%def name="css()">
.avatar {
    margin-left:5px;
}
</%def>

<%def name="title()">
    ${article.title} - JGuoer Lab
</%def>

<%def name="keywords()">
        <meta name="keywords" content="${article.title},JGuoer,Lab" />
</%def>

<%def name="content()">
        <meta name="description" content="${article.content[:100]}" />
</%def>
