# Groups & multiplayer (shared context)

Direct-link / Main apps carry chat context: `chat_type` (`sender|private|group|supergroup|channel`), `chat_instance` (global per-chat id), `start_param` (`tgWebAppStartParam`).

## Patterns

- Open in chat: `https://t.me/<bot>/<app>?startapp=order_123` or `https://t.me/<bot>?startapp=order_123&mode=compact` (half-height).
- Frontend reads `initData.chat_type/chat_instance/start_param` (validated server-side!) to scope state: whiteboard room, group order, game lobby.
- Concurrent use: key all realtime state by `chat_instance`, not `user.id` alone. Multiple members share one room.
- Join-request guard bots: `sendChatJoinRequestWebApp` → `answerChatJoinRequestQuery`.
- Inline mode for sending content: `switchInlineQuery` + `answerInlineQuery` with `InlineQueryResultsButton web_app`.

## Realtime

- Poll or websocket keyed `chat_instance`. Include `chat_instance` in every `Authorization: tma` request's validated payload check (don't trust client-sent room id alone — intersect with initData).
- Show member list via backend (bot `getChatMember`), never expose full member data to clients that shouldn't see it.

## Test

- Create 2 test users + 1 group, open same `?startapp=room_X` link from both, verify shared state converges. Log excerpts required (self-verification rule).
