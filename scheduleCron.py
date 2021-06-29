from crontab import CronTab
 
my_cron = CronTab(tabfile='testing.txt')

job = my_cron.new(command='python scrape.py')
job.hour.every(2)
 
my_cron.write()
