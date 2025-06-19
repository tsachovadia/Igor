# תיעוד מערכת Ultimate Brain

אני איגור, העוזר האישי שלך. להלן תיעוד של מערכת ה-"Ultimate Brain" שלך ב-Notion, כפי שביקשת. התיעוד מבוסס על הסריקה שביצעתי.

## מבנה המערכת

המערכת בנויה סביב דף ראשי בשם "Ultimate Brain for Notion" המשמש כמרכז בקרה (Dashboard). דף זה מחולק לשלוש עמודות עיקריות המכילות קישורים לדפים ותצוגות מרכזיות:

### 1. Dashboards
- **Dashboard**: לוח המחוונים הראשי.
- **My Day**: תצוגה ממוקדת ליום הנוכחי.
- **Quick Capture**: אזור לקליטה מהירה של משימות ורעיונות.
- **Process**: אזור לעיבוד מידע.
- **Plan**: אזור לתכנון.

### 2. Productivity Views
אלו הם ככל הנראה מאגרי המידע או תצוגות מסוננות של מאגרי מידע:
- **Task Manager**: ניהול משימות.
- **Notes**: ניהול פתקים.
- **Projects**: ניהול פרויקטים.
- **Areas**: ניהול תחומי אחריות.
- **Resources**: ניהול משאבים.
- **Goals**: ניהול מטרות.
- **Archive**: ארכיון.

### 3. Special Views
- **Quick Links**: קישורים מהירים.
- **Book Tracker**: מעקב אחר ספרים.
- **Recipe Book**: ספר מתכונים.
- **Scratchpad**: דף טיוטה.
- **Ultimate Brain Lite**: גרסה קלה של המערכת.

---

## מאגר מידע מרכזי: All Tasks [UB]

זהו מאגר המידע הראשי (`master database`) שמפעיל את כל המערכת. כל שאר התצוגות הן למעשה תצוגות מסוננות של מאגר מידע זה.

**מזהה מאגר המידע:** `13f6cd2d-3715-477a-bb89-1a9be066462c`

### מאפיינים (Properties)

להלן רשימת כל המאפיינים במאגר המידע, כולל סוג המאפיין והנוסחאות המלאות.

| שם המאפיין (עברית) | שם מקורי (אנגלית) | סוג | אפשרויות / נוסחה |
| --- | --- | --- | --- |
| משימה | Task | `title` | |
| עדיפות | Priority | `status` | **אפשרויות:** `🚨HIGH`, `🧀 Medium`, `🧊 Low` |
| רשימה חכמה (נוסחה) | Smart List (Formula) | `formula` | `ifs(prop("Due"), "Calendar", prop("Smart List") == "Do Next" or prop("Smart List") == "Delegated", prop("Smart List"), prop("Snooze"), "Snoozed", prop("Smart List") == "Someday", prop("Smart List"), "Inbox")` |
| נוצר | Created | `created_time` | |
| מצב | State | `formula` | `ifs(prop("Parent Task"), "→ ") + ifs(prop("Done"), "😀", not prop("Due"), "⚪", prop("Due").dateEnd().formatDate("L") == now().dateEnd().formatDate("L"), "🟢", prop("Due").dateEnd() < now(), "🔴", now() > prop("Due").dateStart() and now() < prop("Due").dateEnd(), "🟡", "🔵")` |
| תאריך יעד הבא (API) | Next Due API | `formula` | `if(test(prop("Next Due"), "Error") or empty(prop("Next Due")) or prop("Next Due") == false, "∅", "{\"start\":\"" + formatDate(dateStart(prop("Next Due")), "YYYY-MM-DD") + "\",\"end\":\"" + formatDate(dateEnd(prop("Next Due")), "YYYY-MM-DD") + "\"}")` |
| המתן (הורה) | Wait (Parent) | `formula` | `!prop("Parent Task").first().prop("Wait Date") ? prop("Wait Date").timestamp() : prop("Parent Task").first().prop("Wait Date").timestamp()` |
| נוצר על ידי | Created By | `created_by` | |
| פרויקט עדיפות | Priority Project | `rollup` | (Rollup of `Priority` from `Project`) |
| תאריך המתנה | Wait Date | `date` | |
| תג קנבן | Kanban - Tag | `select` | **אפשרויות:** `Design`, `Copy`, `Speed`, `Security` |
| פרויקט הורה | Parent Project | `rollup` | (Rollup of `Project` from `Parent Task`) |
| קר | Cold | `formula` | `prop("Due") ? now().dateBetween(prop("Due"), "days") > 14 and not prop("Done") and prop("Priority") != "🚨HIGH" : false` |
| רשימת הורים חכמה | Parent Smart List | `rollup` | (Rollup of `Smart List (Formula)` from `Parent Task`) |
| הקשרים | Contexts | `multi_select` | **אפשרויות:** `בבסיס`, `סידורים שאני יכול וצריך לעשות שיש לי זמן בלפטופ`, `FUN`, `High-Energy`, `Low-Energy`, `סיבוב סידורים בחוץ`, `Home`, `בבית של ההורים`, `Social` |
| נודניק | Snooze | `date` | |
| תאריך יעד הבא | Next Due | `formula` | (נוסחה ארוכה מאוד לחישוב תאריכים חוזרים) |
| תיבת לכידה מהירה | Quick Capture Box | `formula` | `now().dateBetween(prop("Created"), "days") < 1` |
| ימים (רק אם מוגדר ליום אחד) | Days (Only if Set to 1 Day(s)) | `multi_select` | **אפשרויות:** `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday`, `Sunday` |
| Sub Seed | Sub Seed | `formula` | `not prop("Parent Task")` |
| נערך לאחרונה | Last edited time | `last_edited_time` | |
| בוצע | Done | `checkbox` | |
| מפריד | Divider | `formula` | `"■■■".style("red") + " Everything below here just runs the template".style("b")` |
| איחור | Late | `formula` | `now().dateBetween(prop("Due"), "days") > 0 and not prop("Done") ? "☠️" : ""` |
| יחידת חזרה | Recur Unit | `select` | **אפשרויות:** `Day(s)`, `Week(s)`, `Month(s)`, `Month(s) on the First Weekday`, `Month(s) on the Last Weekday`, `Month(s) on the Last Day`, `Year(s)` |
| סוג | Type | `formula` | `not prop("Recur Interval") ? "⏳One-Time" : "🔄Recurring"` |
| פרויקט | Project | `relation` | (Related to database `94e3f796-ffc0-469d-9c3d-44271d1f2d2b`) |
| תאריך יעד | Due | `date` | |
| מפריד תת-משימה | ✅ Sub-Task Divider | `formula` | `"■■■".style("red") + " Helper functions for sub-task sorting".style("b")` |
| מפתח לוקליזציה | Localization Key | `formula` | (מכיל מחרוזות טקסט לימות השבוע ויחידות זמן לצורך תמיכה בריבוי שפות) |
| חותמת עריכה (הורה) | Edited Stamp (Parent) | `formula` | `!prop("Parent Task") ? prop("Last edited time").timestamp() : prop("Parent Task").first().prop("Last edited time").timestamp()` |
| מרווח חזרה | Recur Interval | `number` | |
| חותמת יצירה (הורה) | Created Stamp (Parent) | `formula` | `!prop("Parent Task") ? prop("Created").timestamp() : prop("Parent Task").first().prop("Created").timestamp()` |
| התחלה | Start | `date` | |
| אזור פרויקט | Project Area | `rollup` | (Rollup of `Area` from `Project`) |
| ספירת תת-משימות | Sub-Task Count | `rollup` | (Rollup of `Task` from `Sub-Tasks`) |
| חותמת זמן יעד | Due Timestamp | `formula` | `!prop("Due") ? now().dateAdd(100, "years").timestamp() : prop("Due").timestamp()` |
| אחראי | Assignee | `people` | |
| נודניק (הורה) | Snooze (Parent) | `formula` | `!prop("Parent Task").first().prop("Snooze") ? prop("Snooze").timestamp() : prop("Parent Task").first().prop("Snooze").timestamp()` |
| משימת הורה | Parent Task | `relation` | (Related to self) |
| תת-משימות | Sub-Tasks | `relation` | (Related to self) |
| רשימה חכמה | Smart List | `select` | **אפשרויות:** `Do Next`, `Delegated`, `Someday` |
| סטטוס קנבן | Kanban Status | `status` | **אפשרויות:** `To Do`, `Doing`, `Done` |
| היסט זמן (UTC) | UTC Offset | `formula` | `0` |
| חותמת יעד (הורה) | Due Stamp (Parent) | `formula` | `!prop("Parent Task") ? prop("Due Timestamp") : prop("Parent Task").first().prop("Due Timestamp")` |
| שם Sub Seed | Sub Seed Name | `formula` | `not prop("Parent Task") and prop("Sub Seed") ? prop("Task").lower() : prop("Parent Task").format().lower()` |
| פתק | Note | `rich_text` | |

---

זוהי התמונה המלאה של מבנה מאגר המידע המרכזי שלך. מכאן, נוכל לחשוב יחד על פונקציונליות נוספת שאוכל לספק לך. למשל, אוכל לעזור לך:
- למצוא משימות ספציפיות.
- לסכם את המשימות הפתוחות בפרויקט מסוים.
- להציג משימות שמתקרבות לתאריך היעד שלהן.
- להוסיף משימות חדשות במהירות.

מה דעתך? 