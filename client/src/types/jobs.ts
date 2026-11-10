export interface SkillType {
  id: number;
  name: string
}

export interface JobType {
  id: number;
  title: string;
  salary_min: number;
  salary_max: number;
  country: string;
  qualification: number,
  experience: number,
  skills?: SkillType[]
}
