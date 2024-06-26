import { createClient, print } from 'redis';

const client = createClient();
client.on('error', err => console.log(`Redis client not connected to the server: ${err}`))

client.on('connect', () => console.log('Redis client connected to the server'));

function setting_hset(arg1, arg2) {
	client.hset('HolbertonSchools', arg1, arg2, print);
}

function main() {
	setting_hset('Portland', 50);
	setting_hset('Seattle', 80);
	setting_hset('New York', 20);
	setting_hset('Bogota', 20);
	setting_hset('Cali', 40);
	setting_hset('Paris', 2);
	client.hgetall('HolbertonSchools', (err, reply) => {
		console.log(reply);
	});
}

main();
