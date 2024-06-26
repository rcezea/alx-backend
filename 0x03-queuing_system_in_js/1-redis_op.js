import { createClient, print } from 'redis';

const client = createClient();
client.on('error', err => console.log(`Redis client not connected to the server: ${err}`))

client.on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
	client.set(schoolName, value, print);
}

function displaySchoolValue(schoolName) {
	const value = client.get(schoolName, (err, val) => {
		if (err) {
			console.error(err);
		}
		console.log(val);
	});
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
