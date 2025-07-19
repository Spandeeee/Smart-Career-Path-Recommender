def get_roadmap(career):
    roadmaps = {
        "Software Engineer": [
            "Learn Python and Data Structures",
            "Build Projects (Web, AI, etc.)",
            "Internships",
            "Apply to companies or start freelancing"
        ],
        "Doctor": [
            "Complete NEET Exam",
            "MBBS (5 years)",
            "Internship",
            "Specialization"
        ],
    }
    return roadmaps.get(career, ["Career roadmap coming soon..."])
