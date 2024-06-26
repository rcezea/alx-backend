import { createClient } from 'redis';
const util = require('util');

const client = createClient();
client.on('error', err => console.log(`Redis client not connected to the server: ${err}`))

client.on('connect', () => console.log('Redis client connected to the server'));

client.get = util.promisify(client.get)
client.set = util.promisify(client.set)

async function setNewSchool(schoolName, value) {
	const res = await client.set(schoolName, value);
	console.log(`Reply: ${res}`);
}

async function displaySchoolValue(schoolName) {
	const value = await client.get(schoolName)
	console.log(value);
}

function main() {
	displaySchoolValue('Holberton');
	setNewSchool('HolbertonSanFrancisco', '100');
	displaySchoolValue('HolbertonSanFrancisco');
}

main();
