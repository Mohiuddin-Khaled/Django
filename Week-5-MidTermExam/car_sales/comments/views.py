from django.views.generic import DetailView
from car.models import CarModel
from comments.forms import CommentForm
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


class CarInfo(DetailView):
    model = CarModel
    pk_url_kwarg = "id"
    template_name = "car_detail.html"
    success_url = reverse_lazy("car_comments")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car_info = self.object
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car_data = self.object
        comments = car_data.comments.all()
        comment_form = CommentForm()
        context["car_data"] = car_data
        context["comments"] = comments
        context["comment_form"] = comment_form
        return context


@login_required
def UpdateQuantity(request, car_id):
    car = get_object_or_404(CarModel, id=car_id)
    car.quantity -= 1
    car.car_buyer.add(request.user)
    car.save()
    return redirect("user_profile")
