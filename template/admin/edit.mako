<%inherit file="/base.mako"/>
<%namespace name="utils" file="/widgets/banner.mako" />

<%def name="main()">
${utils.banner(user.name)}
<form id="editart" action="/admin/edit/${article.id}" method="post" st="${article.cate}" aid="${article.id}">
<div class="info">修改${article.title}</div>
<table>
<tr>
    <td class="titles">标题:</td>
    <td>
        <input type="text" name="title" id="title" class="input" value="${article.title}" desc="添加一个产品的标题，为必填项目"/><span class="needed">*</span>
    </td>
</tr>
<tr>
    <td class="titles">分类:</td>
    <td>
        <input desc="这是一个展示新闻的文章" type="radio" name="cate" value="0"/> 新闻
        <input desc="这是一个展示设计的文章" type="radio" name="cate" value="1"/> 设计
        <input desc="这是一个展示产品的文章" type="radio" name="cate" value="2"/> 产品
    </td>
</tr>
<tr>
    <td class="titles">Url:</td>
    <td>
        <input type="text" name="url" value="${article.url or ''}" class="input" id="url" desc="选择一个外链的Url，填写后点击该文章标题会跳转到外链网站"/><br/>
    </td>
</tr>
<tr>
    <td>内容:</td>
    <td>
    </td>
</tr>
<tr>
    <td colspan="2">
        <textarea class="textarea" name="content" id="content" desc="正文">${article.content or ''}</textarea>
    </td>
</tr>
</table>
<input type="hidden" name="author" value="${user.name}"/>
<input type="submit" value="修改内容"/>
<span class="error">${error or ''}</span>
</form>
<script>
(function(){
    $($("input[name='cate']")[${article.cate}]).attr('checked', 'true');
})()
</script>
</%def>
