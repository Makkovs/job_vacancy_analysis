import { $host } from "."

export const fetchJobs = async () => {
  const { data } = await $host.get("/job/");
  return data;
}