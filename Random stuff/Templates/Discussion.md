<%*
let topic = await tp.system.prompt("What's the topic?");
let username = await tp.system.prompt("Your username?");
let comment = await tp.system.prompt("Your comment?");
await tp.file.rename(topic);
-%>
---
topic: <% topic %>
created: <% tp.date.now("YYYY-MM-DD HH:mm") %>
---

---

<% tp.date.now("YYYY-MM-DD HH:mm") %> #comment-<% username %>

<% comment %>

---
