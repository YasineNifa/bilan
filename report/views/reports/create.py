from django.shortcuts import reverse
from django.views.generic.edit import CreateView

from report.forms import ReportModelForm
from report.models import Report


class ReportCreateView(CreateView):
    form_class = ReportModelForm
    model = Report
    model_name = "report"
    name = "reports_create"
    # namespace = "report"

    title = "Create Report"
    template_name = "report/create.html"

    def get_success_url(self):
        return reverse("report:index")

    def form_valid(self, form):
        print("form : ", form)
        user = form.save(commit=False)
        print("user : ", user)
        # user.is_agent = True
        # user.is_organisor = False
        # user.set_password(f"{random.randint(0,10000)}")# set_password will hash the password. better than user.password = "sdjd"
        # user.save()
        # Agent.objects.create(
        #     user=user,
        #     organisation= self.request.user.userprofile
        # )
        # send_mail(
        #     subject= "You are invited to be an agent",
        #     message="You were added as an agent on our CRM. We invite you to login and start working.",
        #     from_email="admin@crm.com",
        #     recipient_list=[user.email]
        # )
        return super(ReportCreateView, self).form_valid(form)