import axios from 'axios';

const baseURL = 'http://127.0.0.1:5000';
const token = window.localStorage.getItem('token');
export const URLS = {
  login: '/auth/login',
  answer: '/survey/answer',
  result: '/survey/result',
  question: '/survey/questions',
  user: '/user'
};


export const HTTP = axios.create({
  baseURL,
  headers: {
    'Authorization': `Bearer ${token}`
  }
});
