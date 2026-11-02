import re


def detect_document_type(text: str) -> tuple[str, str]:
    text_lower = re.sub(r"\s+", " ", text.lower()).strip()

    if not text_lower:
        return "unknown", "No readable text was extracted."

    cover_letter_patterns = [
        r"\bdear\s+(?:hiring\s+manager|recruiter|sir|madam)\b",
        r"\bi am writing to apply\b",
        r"\bthank you for considering my application\b",
        r"\bsincerely\b",
        r"\byours faithfully\b",
    ]

    report_patterns = [
        r"\binternship report\b",
        r"\btable of contents\b",
        r"\bmethodology\b",
        r"\backnowledgement\b",
        r"\babstract\b",
    ]

    resume_patterns = [
        r"\bresume\b",
        r"\bcurriculum vitae\b",
        r"\bprofessional summary\b",
        r"\bwork experience\b",
        r"\beducation\b",
        r"\btechnical skills\b",
        r"\bprojects\b",
        r"\bcertifications\b",
    ]

    cover_hits = sum(bool(re.search(p, text_lower)) for p in cover_letter_patterns)
    report_hits = sum(bool(re.search(p, text_lower)) for p in report_patterns)
    resume_hits = sum(bool(re.search(p, text_lower)) for p in resume_patterns)

    if resume_hits >= 3:
        return "resume", "Resume sections detected."

    if cover_hits >= 2:
        return "cover_letter", "Cover-letter language detected."

    if report_hits >= 3:
        return "internship_report", "Report-style sections detected."

    return "unknown", "Could not confidently identify the document type."