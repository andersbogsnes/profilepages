import axios from 'axios';
const baseURL = 'http://127.0.0.1:5000';

export const URLS = {
  login: '/auth/login',
  answer: '/survey/answer',
  result: '/survey/result',
  question: '/survey/questions',
  user: '/user'
};

export const HTTP = axios.create({
  baseURL
});

export const getUrl = (url) => {
  const token = window.localStorage.getItem('token') || '';
  return HTTP.get(url, {
    headers: {
      "Authorization": `Bearer ${token}`
    }
  })
};

export const postUrl = (url, data) => {
  const token = window.localStorage.getItem('token') || '';
  return HTTP.post(url, data, {
    headers: {
      "Authorization": `Bearer ${token}`
    }
  })
};
