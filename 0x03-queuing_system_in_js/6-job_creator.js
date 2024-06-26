const kue = require('kue');

const queue = kue.createQueue();

const jobData = {
	phoneNumber: '09065046509',
	message: "Message for each queue",
  };

const job = queue.create('push_notification_code', jobData).save(
	(err) => {
		if( !err ) console.log(`Notification job created: ${job.id}` );
	});

job.on('complete', (result) => {
	console.log('Notification job completed');
}).on('failed', (error) => {
	console.log('Notification job failed');
});