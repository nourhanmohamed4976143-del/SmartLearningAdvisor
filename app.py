
import streamlit as st
from collections import Counter

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Smart Student Advisor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# 2. PROFESSIONAL DESIGN
# ==========================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800&display=swap');

.stApp {
    background: linear-gradient(135deg, #0b1020, #14152e 60%, #101c35);
    color: #f4f5ff;
    font-family: 'Cairo', sans-serif;
}
html, body, [class*="css"] {
    font-family: 'Cairo', sans-serif;
}
.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}
.hero {
    background: linear-gradient(120deg, #29235b, #193e62);
    border: 1px solid #514b91;
    border-radius: 25px;
    padding: 32px 24px;
    text-align: center;
    margin-bottom: 25px;
    box-shadow: 0 12px 40px rgba(65, 75, 180, .16);
}
.hero h1 {
    color: white;
    font-size: 38px;
    font-weight: 800;
}
.hero p {
    color: #d8ddff;
    font-size: 16px;
}
.author {
    color: #d4ccff;
    font-size: 15px;
    font-weight: 700;
    margin-top: 15px;
}
.section-card {
    background: #191d38;
    border: 1px solid #343b65;
    border-radius: 18px;
    padding: 22px;
    margin-bottom: 18px;
}
.tip {
    background: #202747;
    border-left: 4px solid #8b7cff;
    border-radius: 10px;
    padding: 14px;
    margin: 8px 0 16px 0;
}
.small-note {
    color: #aeb7da;
    font-size: 13px;
}
div[data-testid="stMetric"] {
    background: #191d38;
    border: 1px solid #343b65;
    border-radius: 15px;
    padding: 18px;
}
div.stButton > button,
div.stDownloadButton > button {
    background: linear-gradient(90deg, #7767f5, #3988ec);
    color: white;
    border: none;
    border-radius: 12px;
    min-height: 45px;
    font-weight: 700;
}
div.stButton > button:hover,
div.stDownloadButton > button:hover {
    border: 1px solid #b7b5ff;
    color: white;
}
div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div {
    background-color: #171b32;
}
h1, h2, h3 {
    color: #f3f4ff;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. SESSION STATE
# ==========================================
if "stage" not in st.session_state:
    st.session_state.stage = None

if "subjects" not in st.session_state:
    st.session_state.subjects = []

if "next_subject_id" not in st.session_state:
    st.session_state.next_subject_id = 1

if "analysis" not in st.session_state:
    st.session_state.analysis = None


def create_subject():
    sid = st.session_state.next_subject_id
    st.session_state.next_subject_id += 1
    return {"id": sid}


def reset_subjects(stage):
    st.session_state.stage = stage
    initial_count = 7 if stage == "school" else 5
    st.session_state.subjects = [
        create_subject() for _ in range(initial_count)
    ]
    st.session_state.analysis = None


# ==========================================
# 4. HEADER
# ==========================================
st.markdown("""
<div class="hero">
    <h1>🎓 Smart Student Advisor</h1>
    <p>Personalized Learning & Smart Study Planning</p>
    <p>مستشارك الدراسي الذكي — خطتك للتطور تبدأ من هنا</p>
    <div class="author">
        Designed & Developed by Eng. Nourhan Mohamed
    </div>
    <p class="small-note">Artificial Intelligence Student</p>
</div>
""", unsafe_allow_html=True)


# ==========================================
# 5. HOME SCREEN
# ==========================================
if st.session_state.stage is None:

    st.markdown("## 👋 أهلاً بيك!")
    st.write(
        "اختار مرحلتك الدراسية، وساعد البرنامج يفهم "
        "احتياجاتك وينظم لك خطة مذاكرة مناسبة."
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
        <div class="section-card">
            <h2>🏫 المدرسة</h2>
            <p>أدخل أسماء المواد ودرجاتك، واعرف المواد
            التي تحتاج إلى تحسين، مع نصائح وخطة مذاكرة.</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "🏫 أنا طالب في المدرسة",
            use_container_width=True
        ):
            reset_subjects("school")
            st.rerun()

    with col2:
        st.markdown("""
        <div class="section-card">
            <h2>🎓 الجامعة</h2>
            <p>قيّم مستواك بنفسك في كل مادة دون إدخال درجات،
            واحصل على نصائح وخطة أسبوعية مخصصة.</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "🎓 أنا طالب في الجامعة",
            use_container_width=True
        ):
            reset_subjects("university")
            st.rerun()

    st.markdown("---")
    st.markdown(
        "<p class='small-note' style='text-align:center;'>"
        "SMART STUDENT ADVISOR • STUDY SMARTER, ACHIEVE MORE"
        "</p>",
        unsafe_allow_html=True
    )


# ==========================================
# 6. SUBJECTS
# ==========================================
else:
    stage = st.session_state.stage
    is_school = stage == "school"
    stage_name = "المدرسة" if is_school else "الجامعة"

    top1, top2 = st.columns([4, 1])

    with top1:
        st.markdown(f"## 📚 بيانات الطالب — {stage_name}")

    with top2:
        if st.button("🏠 الرئيسية", use_container_width=True):
            st.session_state.stage = None
            st.session_state.analysis = None
            st.rerun()

    if is_school:
        st.info(
            "المدرسة: أدخل درجاتك، ويمكنك إضافة أو حذف المواد."
        )
    else:
        st.info(
            "الجامعة: لا توجد درجات أو متوسط عام. "
            "اكتب أسماء المواد وحدد مستواك في كل مادة."
        )

    # ------------------------------------------
    # Add / remove subjects in BOTH stages
    # ------------------------------------------
    add_col, remove_col = st.columns(2)

    with add_col:
        if st.button("➕ إضافة مادة", use_container_width=True):
            st.session_state.subjects.append(create_subject())
            st.session_state.analysis = None
            st.rerun()

    with remove_col:
        if st.button(
            "➖ حذف آخر مادة",
            use_container_width=True,
            disabled=len(st.session_state.subjects) <= 1
        ):
            removed = st.session_state.subjects.pop()
            st.session_state.analysis = None
            st.rerun()

    st.caption(
        f"عدد المواد الحالي: {len(st.session_state.subjects)}"
    )

    st.markdown("### ✍️ بيانات المواد")

    level_options = [
        "محتاج أبدأ من الصفر",
        "ضعيف",
        "متوسط",
        "قوي"
    ]

    for i, subject in enumerate(st.session_state.subjects):
        sid = subject["id"]

        with st.container(border=True):
            st.markdown(f"**المادة {i + 1}**")

            if is_school:
                c1, c2, c3 = st.columns([2, 1, 1])

                with c1:
                    st.text_input(
                        "اسم المادة",
                        key=f"name_{sid}",
                        placeholder="اكتب اسم المادة"
                    )

                with c2:
                    st.number_input(
                        "درجتك",
                        min_value=0.0,
                        value=0.0,
                        step=1.0,
                        key=f"score_{sid}"
                    )

                with c3:
                    st.number_input(
                        "الدرجة النهائية",
                        min_value=1.0,
                        value=100.0,
                        step=1.0,
                        key=f"total_{sid}"
                    )

            else:
                c1, c2 = st.columns([2, 1])

                with c1:
                    st.text_input(
                        "اسم المادة",
                        key=f"name_{sid}",
                        placeholder="اكتب اسم المادة"
                    )

                with c2:
                    st.selectbox(
                        "قيّم مستواك",
                        options=level_options,
                        index=2,
                        key=f"level_{sid}"
                    )

    # ==========================================
    # 7. STUDY PREFERENCES
    # ==========================================
    st.markdown("## ⏰ وقت المذاكرة المتاح")

    p1, p2 = st.columns(2)

    with p1:
        study_hours = st.selectbox(
            "عدد ساعات المذاكرة يوميًا",
            [1, 2, 3, 4, 5, 6, 7, 8],
            index=2,
            format_func=lambda x: f"{x} ساعة"
        )

    with p2:
        study_days = st.selectbox(
            "أيام المذاكرة أسبوعيًا",
            [3, 4, 5, 6, 7],
            index=3,
            format_func=lambda x: f"{x} أيام"
        )

    if is_school:
        pass_mark = st.slider(
            "درجة النجاح (%)",
            min_value=30,
            max_value=70,
            value=50
        )
    else:
        pass_mark = None

    st.markdown("---")

    # ==========================================
    # 8. ANALYSIS
    # ==========================================
    if st.button(
        "✨ تحليل المستوى وإنشاء خطة المذاكرة",
        use_container_width=True
    ):
        records = []
        errors = []

        for i, subject in enumerate(st.session_state.subjects):
            sid = subject["id"]
            name = st.session_state.get(
                f"name_{sid}", ""
            ).strip()

            if not name:
                errors.append(f"اكتب اسم المادة رقم {i + 1}.")
                continue

            if is_school:
                score = st.session_state.get(
                    f"score_{sid}", 0.0
                )
                total = st.session_state.get(
                    f"total_{sid}", 100.0
                )

                if total <= 0 or score < 0 or score > total:
                    errors.append(
                        f"راجع الدرجات في مادة {name}."
                    )
                    continue

                percentage = score / total * 100

                if percentage < pass_mark:
                    level = "يحتاج إلى تحسين"
                    weight = 4
                elif percentage < 70:
                    level = "متوسط"
                    weight = 3
                elif percentage < 85:
                    level = "جيد جدًا"
                    weight = 2
                else:
                    level = "ممتاز"
                    weight = 1

                records.append({
                    "name": name,
                    "score": score,
                    "total": total,
                    "percentage": percentage,
                    "level": level,
                    "weight": weight
                })

            else:
                level = st.session_state.get(
                    f"level_{sid}", "متوسط"
                )

                weights_by_level = {
                    "محتاج أبدأ من الصفر": 4,
                    "ضعيف": 3,
                    "متوسط": 2,
                    "قوي": 1
                }

                records.append({
                    "name": name,
                    "level": level,
                    "weight": weights_by_level[level]
                })

        names = [r["name"].casefold() for r in records]

        if len(names) != len(set(names)):
            errors.append(
                "يوجد تكرار في أسماء المواد. "
                "عدّل الأسماء لتكون مميزة."
            )

        if errors:
            for error in errors:
                st.error(error)
            st.session_state.analysis = None

        elif not records:
            st.warning("أدخل بيانات مادة واحدة على الأقل.")

        else:
            if is_school:
                records.sort(key=lambda r: r["percentage"])

            st.session_state.analysis = {
                "records": records,
                "stage": stage,
                "study_hours": study_hours,
                "study_days": study_days,
                "pass_mark": pass_mark
            }

    # ==========================================
    # 9. RESULTS AND PERSONALIZED ADVICE
    # ==========================================
    result = st.session_state.analysis

    if result and result["stage"] == stage:
        records = result["records"]
        study_hours = result["study_hours"]
        study_days = result["study_days"]

        weekly_minutes = study_hours * 60 * study_days

        st.markdown("---")
        st.markdown("## 📊 تحليل المستوى")

        if is_school:
            average = sum(
                r["percentage"] for r in records
            ) / len(records)

            needs_work = sum(
                r["percentage"] < pass_mark for r in records
            )

            m1, m2, m3 = st.columns(3)
            m1.metric("المتوسط العام", f"{average:.1f}%")
            m2.metric("عدد المواد", len(records))
            m3.metric("مواد تحتاج تحسين", needs_work)

            if average >= 85:
                st.success(
                    "مستواك جيد جدًا! استمر في المراجعة "
                    "والتدريب للحفاظ على تقدمك."
                )
            elif average >= pass_mark:
                st.info(
                    "مع تنظيم وقتك والتركيز على نقاط الضعف، "
                    "يمكنك تحسين مستواك."
                )
            else:
                st.warning(
                    "ابدأ بالمواد التي تحتاج إلى تحسين، "
                    "وقسّم كل مادة إلى أجزاء صغيرة."
                )

        else:
            counts = Counter(r["level"] for r in records)

            m1, m2, m3 = st.columns(3)
            m1.metric("إجمالي المواد", len(records))
            m2.metric(
                "مواد تحتاج أولوية",
                counts["ضعيف"] + counts["محتاج أبدأ من الصفر"]
            )
            m3.metric("مواد قوية", counts["قوي"])

            if counts["محتاج أبدأ من الصفر"] or counts["ضعيف"]:
                st.warning(
                    "ابدأ بالمواد التي قيّمت مستواك فيها "
                    "بضعيف أو تحتاج إلى البدء من الصفر."
                )
            elif counts["متوسط"]:
                st.info(
                    "ركّز على تحسين المواد المتوسطة، "
                    "مع الاستمرار في مراجعة المواد القوية."
                )
            else:
                st.success(
                    "قيّمت كل موادك بأنها قوية. حافظ على مستواك "
                    "باختبارات ذاتية وأسئلة متقدمة."
                )

        st.markdown("### 📚 مستوى كل مادة ونصائحها")

        advice = {
            "محتاج أبدأ من الصفر": (
                "ابدأ بالأساسيات والمتطلبات السابقة، "
                "وافهم جزءًا صغيرًا كل مرة. اكتب ملخصًا "
                "بكلماتك، ثم حل أسئلة سهلة قبل الانتقال للأصعب."
            ),
            "ضعيف": (
                "راجع المحاضرة أو الكتاب، وحدد النقاط غير "
                "الواضحة. حل من 5 إلى 10 أسئلة مناسبة، "
                "وسجّل أخطاءك وراجع أسبابها."
            ),
            "متوسط": (
                "اختبر نفسك دون النظر إلى الملاحظات، "
                "وتدرّب على أسئلة متنوعة. خصص وقتًا للأجزاء "
                "التي ما زلت تتردد فيها."
            ),
            "قوي": (
                "حافظ على مستواك بالمراجعة المتباعدة، "
                "وحل أسئلة أكثر تحديًا، وحاول شرح الموضوع "
                "بكلماتك كأنك تدرّسه لشخص آخر."
            )
        }

        for r in records:
            if is_school:
                level_key = (
                    "محتاج أبدأ من الصفر"
                    if r["percentage"] < pass_mark
                    else "ضعيف"
                    if r["percentage"] < 70
                    else "متوسط"
                    if r["percentage"] < 85
                    else "قوي"
                )
                st.markdown(
                    f"**{r['name']}** — {r['percentage']:.1f}% "
                    f"— {r['level']}"
                )
            else:
                level_key = r["level"]
                st.markdown(
                    f"**{r['name']}** — مستواك: {r['level']}"
                )

            st.markdown(
                f"<div class='tip'>"
                f"💡 <b>نصيحة:</b> {advice[level_key]}"
                f"</div>",
                unsafe_allow_html=True
            )

        # ==========================================
        # 10. WEEKLY STUDY PLAN
        # ==========================================
        st.markdown("---")
        st.markdown("## 🗓️ خطة المذاكرة الأسبوعية")

        st.write(
            "الخطة توزّع وقتك المتاح على المواد، "
            "مع تخصيص وقت أكبر للمواد التي تحتاج إلى دعم."
        )

        total_weight = sum(r["weight"] for r in records)

        # Allocate whole minutes without exceeding weekly total.
        allocations = []
        for r in records:
            exact = weekly_minutes * r["weight"] / total_weight
            allocations.append({
                "name": r["name"],
                "weight": r["weight"],
                "minutes": int(exact),
                "remainder": exact - int(exact),
                "level": r["level"]
            })

        remaining = weekly_minutes - sum(
            a["minutes"] for a in allocations
        )

        for item in sorted(
            allocations,
            key=lambda a: a["remainder"],
            reverse=True
        )[:remaining]:
            item["minutes"] += 1

        # Distribute each subject's time over all study days.
        day_names = [
            "اليوم الأول", "اليوم الثاني", "اليوم الثالث",
            "اليوم الرابع", "اليوم الخامس", "اليوم السادس",
            "اليوم السابع"
        ]

        daily_plan = [[] for _ in range(study_days)]

        for item in allocations:
            base = item["minutes"] // study_days
            extra = item["minutes"] % study_days

            for day in range(study_days):
                minutes = base + (1 if day < extra else 0)
                if minutes > 0:
                    daily_plan[day].append({
                        "name": item["name"],
                        "minutes": minutes,
                        "level": item["level"]
                    })

        for day in range(study_days):
            st.markdown(
                f"<div class='section-card'>"
                f"<h3>📅 {day_names[day]}</h3>"
                f"</div>",
                unsafe_allow_html=True
            )

            if not daily_plan[day]:
                st.write("راحة أو مراجعة خفيفة حسب احتياجك.")
                continue

            for item in daily_plan[day]:
                if item["level"] in [
                    "ضعيف", "محتاج أبدأ من الصفر",
                    "يحتاج إلى تحسين"
                ]:
                    activity = (
                        "فهم الأساسيات، مذاكرة جزء صغير، "
                        "وحل تدريبات مناسبة."
                    )
                elif item["level"] in ["متوسط", "جيد جدًا"]:
                    activity = (
                        "مراجعة مركزة، تطبيق عملي، "
                        "واختبار ذاتي."
                    )
                else:
                    activity = (
                        "مراجعة سريعة وأسئلة متنوعة "
                        "للحفاظ على المستوى."
                    )

                st.markdown(
                    f"- **{item['name']}** — "
                    f"{item['minutes']} دقيقة: {activity}"
                )

        st.info(
            f"إجمالي الوقت المتاح: {study_hours} ساعة يوميًا × "
            f"{study_days} أيام = {weekly_minutes // 60} ساعة "
            f"و{weekly_minutes % 60} دقيقة أسبوعيًا."
        )

        st.markdown("### ✅ نصائح للالتزام بالخطة")
        st.write("1. ابدأ بالمادة الأصعب عندما يكون تركيزك أفضل.")
        st.write("2. خذ استراحة قصيرة بين جلسات المذاكرة.")
        st.write("3. حل أسئلة بعد كل جزء، بدلًا من القراءة فقط.")
        st.write("4. راجع الأخطاء القديمة بشكل منتظم.")
        st.write("5. عدّل تقييمك وخطتك عندما تلاحظ تحسنًا.")

        # ==========================================
        # 11. DOWNLOADABLE REPORT
        # ==========================================
        report = [
            "SMART STUDENT ADVISOR",
            "Personalized Study Report",
            "Designed & Developed by Eng. Nourhan Mohamed",
            "=" * 45,
            f"Stage: {stage_name}",
            f"Study hours per day: {study_hours}",
            f"Study days per week: {study_days}",
            f"Total weekly minutes: {weekly_minutes}",
            "",
            "SUBJECT ANALYSIS"
        ]

        if is_school:
            report.append(f"Overall average: {average:.1f}%")
            report.append(f"Pass mark: {pass_mark}%")

        for r in records:
            if is_school:
                report.append(
                    f"{r['name']}: {r['score']}/{r['total']} "
                    f"({r['percentage']:.1f}%) - {r['level']}"
                )
            else:
                report.append(f"{r['name']}: {r['level']}")

            level_key = (
                "محتاج أبدأ من الصفر"
                if is_school and r["percentage"] < pass_mark
                else "ضعيف"
                if is_school and r["percentage"] < 70
                else "متوسط"
                if is_school and r["percentage"] < 85
                else "قوي"
                if is_school
                else r["level"]
            )
            report.append(f"Advice: {advice[level_key]}")
            report.append("")

        report.append("WEEKLY STUDY PLAN")
        for day in range(study_days):
            report.append(f"\n{day_names[day]}")
            for item in daily_plan[day]:
                report.append(
                    f"- {item['name']}: {item['minutes']} minutes"
                )

        st.download_button(
            "📥 تحميل تقرير المستوى وخطة المذاكرة",
            data="\n".join(report),
            file_name="smart_study_plan.txt",
            mime="text/plain",
            use_container_width=True
        )

        if st.button(
            "🔄 إعادة التحليل",
            use_container_width=True
        ):
            st.session_state.analysis = None
            st.rerun()


# ==========================================
# 12. FOOTER
# ==========================================
st.markdown("---")
st.markdown("""
<div style="text-align:center; padding:15px;">
    <p style="color:#aeb7da;">🎓 SMART STUDENT ADVISOR</p>
    <p style="color:#d4ccff; font-weight:700;">
        Designed & Developed by Eng. Nourhan Mohamed
    </p>
    <p style="color:#aeb7da; font-size:13px;">
        Study smarter. Improve every day.
    </p>
</div>
""", unsafe_allow_html=True)
