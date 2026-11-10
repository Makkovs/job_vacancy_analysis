import { $host } from ".";

export const fetchSkills = async () => {
  const { data } = await $host.get("skill/");
  return data;
}