from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Video
from .forms import VideoForm

def videos_list(request):
    videos = Video.objects.all()
    context = {
        "videos": videos
    }
    return render(request, "videos_list.html", context)

@login_required
def video_upload(request):
    if request.method == "POST":
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.autor = request.user
            video.save()
            return redirect("videos_list")
    else:
        form = VideoForm()
    context = {
        "form": form
    }
    return render(request, "video_upload.html", context)
