<%*
  // Prompt for the topic
  let topic = await tp.system.prompt("Enter the topic:");
  
  // Prompt for username (the person leaving the comment)
  let username = await tp.system.prompt("Enter your username:");
  
  // Prompt for the initial message content
  let initialContent = await tp.system.prompt("Enter initial content:");
  
  // Get current date/time in YYYY-MM-DD HH:mm format
  let now = new Date();
  let pad = (n) => (n < 10 ? '0' + n : n);
  let year = now.getFullYear();
  let month = pad(now.getMonth() + 1);
  let day = pad(now.getDate());
  let hours = pad(now.getHours());
  let minutes = pad(now.getMinutes());
  let dateTime = `${year}-${month}-${day} ${hours}:${minutes}`;
  
  // Rename the file to the topic
  await tp.file.rename(topic);
%>
---
date: "<%* tR = dateTime; tR %>"
topic: "<%* tR = topic; tR %>"
---

### <% dateTime %> - #comment-<% username %>
<% initialContent %>

---
Corporate structure"
---

### 2024-12-18 14:14 - #comment-greg
Should we setup 1 or 2 companies

---
