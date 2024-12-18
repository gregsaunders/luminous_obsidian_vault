<%*
let username = await tp.system.prompt("Your username?");
let comment = await tp.system.prompt("Your comment?");
-%>

<% tp.date.now("YYYY-MM-DD HH:mm") %> #comment-<% username %>

<% comment %>

---
