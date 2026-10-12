const tg = (window as any).Telegram?.WebApp;
if (tg) {
  tg.ready();
  const paint = () => {
    document.documentElement.style.background = tg.themeParams?.bg_color ?? "#fff";
    tg.setHeaderColor?.(tg.themeParams?.bg_color ?? "#ffffff");
    tg.setBackgroundColor?.(tg.themeParams?.bg_color ?? "#ffffff");
  };
  paint();
  tg.onEvent?.("themeChanged", paint);
}
export async function authFetch(path: string, body?: unknown) {
  const raw = tg?.initData ?? "";
  const res = await fetch(path, { method: body ? "POST" : "GET",
    headers: { "Content-Type": "application/json", ...(raw ? { Authorization: `tma ${raw}` } : {}) },
    ...(body ? { body: JSON.stringify(body) } : {}) });
  if (!res.ok) throw new Error(`API ${res.status}`);
  return res.json();
}
document.getElementById("app")!.innerHTML = "<h1>Mini App base</h1><p>Replace with shop/booking/game screen.</p>";
