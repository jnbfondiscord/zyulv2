document.getElementById("submit").addEventListener("click", async () => {
  const code = document.getElementById("code").value;
  const res = await fetch("/api/update", {
    method: "POST",
    body: code
  });
  const msg = await res.text();
  alert(msg);
});
