# Vite config for Mini Apps

```ts
import { defineConfig } from 'vite';
export default defineConfig(({ mode }) => ({
  base: './',                       // REQUIRED: relative asset paths (?startapp breaks absolute /assets)
  server: { host: true, port: 5173, strictPort: true },
  build: { outDir: 'dist', sourcemap: false, chunkSizeWarningLimit: 600,
    rollupOptions: { output: { manualChunks: { three: ['three'] } } } }, // 3D never in main chunk
  preview: { host: true, port: 4173 },
}));
```

Dev flows:
- Plain local (browser only): `npm run dev -- --host --port 5173`.
- Desktop-with-cert (NOT mobile): add `@vitejs/plugin-basic-ssl` and `npm run dev:https`. Expect untrusted-cert warning; Android/iOS will still white-screen — use a tunnel (see local-run.md).
- Tunnel (real test): plain `npm run dev` + `cloudflared tunnel --url http://localhost:5173`.

Build checks before handing URL to the bot: `npm run build && npx vite preview --host --port 4173`, then `curl -I http://localhost:4173` → 200 and no absolute `/assets/` paths in `dist/index.html` (`grep -o 'src="/' dist/index.html` must be empty).
