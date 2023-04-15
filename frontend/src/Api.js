import axios from 'axios';

const baseURL = 'http://localhost:5123';

const Api = axios.create({
	baseURL: baseURL,
	timeout: 5000,
});

export default Api;
