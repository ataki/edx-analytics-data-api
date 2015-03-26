from django.conf.urls import patterns, url

from analytics_data_api.v0.views import courses as views

COURSE_ID_PATTERN = r'(?P<course_id>[^/+]+[/+][^/+]+[/+][^/]+)'
COURSE_URLS = [
    ('activity', views.CourseActivityWeeklyView, 'activity'),
    ('recent_activity', views.CourseActivityMostRecentWeekView, 'recent_activity'),
    ('enrollment', views.CourseEnrollmentView, 'enrollment_latest'),
    ('enrollment/mode', views.CourseEnrollmentModeView, 'enrollment_by_mode'),
    ('enrollment/birth_year', views.CourseEnrollmentByBirthYearView, 'enrollment_by_birth_year'),
    ('enrollment/education', views.CourseEnrollmentByEducationView, 'enrollment_by_education'),
    ('enrollment/gender', views.CourseEnrollmentByGenderView, 'enrollment_by_gender'),
    ('enrollment/location', views.CourseEnrollmentByLocationView, 'enrollment_by_location'),
    ('problems', views.ProblemsListView, 'problems'),
    ('videos', views.CourseVideoListView, 'videos'),
    ('on_campus_student_data', views.OnCampusStudentDataView, 'on_campus_student_data'),
]

# TODO Check correctness of video id regex
COURSE_VIDEO_ID_PATTERN = r'(?P<video_id>[A-Za-z0-9\-]+[^/]+)'
COURSE_VIDEO_URLS = [
    ('seek_times', views.CourseVideoSeekTimesView, 'course_video_seek_times'),
]

urlpatterns = []

for path, view, name in COURSE_URLS:
    regex = r'^{0}/{1}/$'.format(COURSE_ID_PATTERN, path)
    urlpatterns += patterns('', url(regex, view.as_view(), name=name))

for path, view, name in COURSE_VIDEO_URLS:
    regex = r'^videos/{0}/{1}/$'.format(COURSE_VIDEO_ID_PATTERN, path)
    urlpatterns += patterns('', url(regex, view.as_view(), name=name))
