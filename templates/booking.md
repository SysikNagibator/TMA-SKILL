# booking — slots + form + confirm

Screens: Service → Slots (date strip + time grid, selection haptic) → Form (name/phone, `closingConfirmation` when dirty) → Confirm (BottomButton "Book", `requestWriteAccess` on tap with reason "reminders").
API: `GET /api/slots?day=`, `POST /api/book` (server-side slot lock, 409 on conflict).
Empty: "No slots — pick another day". Error: "Slot just taken — choose new".
