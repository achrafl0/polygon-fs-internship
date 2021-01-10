import axios, { AxiosInstance } from 'axios';

export default function instanciateAxios(): AxiosInstance {
  return axios.create({
    baseURL: 'http://localhost:1337/api/v1',
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Content-Type': 'application/json',
    },
    transformRequest: [(data) => JSON.stringify(data)],
    transformResponse: [(data) => JSON.parse(data)],
  });
}
