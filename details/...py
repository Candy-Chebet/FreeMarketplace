# def job_details(request, job_id):
#     job = get_object_or_404(This_Job, pk=job_id)
#     user = User.objects.all()
#     name = request.user

#     all_bids = Bid.objects.all()

#     emp_all = ProfileEmp.objects.all()
#     free_all = ProfileFree.objects.all()


#     for emp in emp_all:
#         if name == emp.user:
#             emp_user = True
#             break
#         else:
#             emp_user = False

#     for free in free_all:
#         if name == free.user:
#             free_user = True
#             break
#         else:
#             free_user = False


#     #submit bid form
#     if request.method == 'POST':
#         form = Bid_Form(request.POST)
#         if form.is_valid():
#             bid = form.save(commit=False)
#             bid.bid_poster = name
#             bid.job = job
#             bid.save()

#             Message.objects.create(post_user=job.user, comment_user=name, job=job)

#             #return redirect('details:job_details')
#             return HttpResponseRedirect(request.path_info)
#     else:
#         form = Bid_Form()


#     count_bid = 0

#     for bid in all_bids:
#         if job == bid.job:
#             count_bid = count_bid+1

#     for bid in all_bids:
#         if job == bid.job and name == bid.bid_poster:
#             bid_limit = True
#             break
#         else:
#             bid_limit = False

#     all_messages = Message.objects.all()
#     count_message_e = 0

#     for message in all_messages:
#         if name == message.post_user and message.viewed == False:
#             count_message_e = count_message_e + 1


#     context = {
#         'form': form,
#         'user': user,
#         'job': job,
#         'name': name,
#         'all_bids': all_bids,
#         'count_bid': count_bid,
#         'bid_limit': bid_limit,
#         'emp_user': emp_user,
#         'free_user': free_user,
#         'all_messages': all_messages,
#         'count_message_e': count_message_e,

#     }
#     return render(request, 'details/job_details.html', context)