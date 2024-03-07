class JobOrder:
    # NOTE: is RM summary fixed?

    def __init__(self, 
                 job_order: str,
                 event_name: str,
                 venue: str,
                 event_start_date: str,
                 event_end_date: str,
                 ingress_date: str,
                 ingress_time: str,
                 egress_date: str,
                 egress_time: str,
                 client_id: str,
                 approver_id: str,
                 reviewer_id: str):
        self.job_order = job_order
        self.event_name = event_name
        self.venue = venue
        self.event_start_date = event_start_date
        self.event_end_date = event_end_date
        self.ingress_date = ingress_date
        self.ingress_time = ingress_time
        self.egress_date = egress_date
        self.egress_time = egress_time
        self.client_id = client_id
        self.approver_id = approver_id
        self.reviewer_id = reviewer_id

    def __str__(self):
        return f'{self.job_order}'