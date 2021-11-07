class WorkingPlan:
    def __init__(self, lecturing, conducting_practics_and_seminars, conducting_laboratory_lessons,
                 conducting_clinical_practic_lessons, conducting_individual_lessons, practics,
                 individual_tasks, degree_project, state_attestation, test, exam):
        self.lecturing=lecturing
        self.conducting_practics_and_seminars=conducting_practics_and_seminars
        self.conducting_laboratory_lessons=conducting_laboratory_lessons
        self.conducting_clinical_practic_lessons = conducting_clinical_practic_lessons
        self.conducting_individual_lessons=conducting_individual_lessons
        self.practics = practics
        self.individual_tasks = individual_tasks
        self.degree_project = degree_project
        self.state_attestation=state_attestation
        self.test=test
        self.exam=exam
