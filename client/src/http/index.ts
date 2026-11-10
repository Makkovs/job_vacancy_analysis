import axios from "axios";


const $host = axios.create({
  baseURL: "/api"
});

const $authHost = axios.create({
  baseURL: "/api"
});

const authInterceptor = (config: any) => {
  const token = localStorage.getItem("token") || "";
  config.headers.authorization = `Bearer ${token}`;
  return config;
}

$authHost.interceptors.request.use(authInterceptor);

export {
  $host,
  $authHost
}