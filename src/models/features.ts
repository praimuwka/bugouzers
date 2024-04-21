// models.ts

// EntrantSchema
export interface EntrantSchema {
  is_budget: boolean;
  price?: number;
  jobs?: string[] | null;
  exams: ExamInfo[];
}

// ExamInfo
export interface ExamInfo {
  name: ExamNameEnum;
  mark: number;
}

export interface ExamAdditionalInfo {
  name: ExamNameEnum;
  exams_number: number;
}

// ExamNameEnum
export type ExamNameEnum = "Математика" | "Русский язык" | "Физика" | "Информатика" | "Обществознание" | "Английский язык";

// ValidationError
export interface ValidationError {
  loc: (string | number)[];
  msg: string;
  type: string;
}

// HTTPValidationError
export interface HTTPValidationError {
  detail: ValidationError[];
}
