from sites.models import Site, Detail
from django.db.models import Sum
from django.shortcuts import render


def index(request):  # For page summary and Sum Implemented using python
    site_aggregate = [[0 for x in range(3)] for y in range(Site.objects.count())]  # Initialising matrix
    count = 0
    for site in Site.objects.all():
        site_aggregate[count][0] = site.name
        site_aggregate[count][1] = Detail.objects.filter(site=site.pk).aggregate(Sum('a_value')).get('a_value__sum', 0.00)
        site_aggregate[count][2] = Detail.objects.filter(site=site.pk).aggregate(Sum('b_value')).get('b_value__sum', 0.00)
        count += 1
    context = {
        'site_aggregate': site_aggregate
    }
    return render(request, 'summary/summary.html', context)


def average(request):  # For page summary-average and average. Implemented using django API and raw SQL
    site_aggregate = [[0 for x in range(3)] for y in range(Site.objects.count())]  # Initialising matrix
    count = 0
    for site in Site.objects.all():
        site_aggregate[count][0] = site.name
        averages = Detail.objects.raw('SELECT id, AVG(a_value) AS avg_a, AVG(b_value) AS avg_b FROM sites_Detail WHERE site_name= %s GROUP BY site_name',[site.name])
        for row in averages:
            site_aggregate[count][1] = row.avg_a
            site_aggregate[count][2] = row.avg_b
        count += 1
    context = {
        'site_aggregate': site_aggregate
    }
    return render(request, 'summary/summary.html', context)

