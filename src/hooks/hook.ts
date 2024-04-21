// useGetPrograms.js
import { Ref, ref } from 'vue';
import axios, { AxiosError } from 'axios';
import { EntrantSchema, ExamAdditionalInfo} from 'src/models/features';

export default function useGetData() {
  const data = ref([]);
  const loading = ref(false);
  const error : Ref<string|null> = ref(null);

  const post = async (inp_data: any, url: string) => {
    loading.value = true;
    try {
      // Replace the URL with your actual API endpoint
      const response = await axios.post(url, inp_data);
      data.value = response.data;
    } catch (err) {
      const axiosError = err as AxiosError;
      error.value = axiosError.message;
    } finally {
      loading.value = false;
    }
  };

  return { data, loading, error, post };
}
