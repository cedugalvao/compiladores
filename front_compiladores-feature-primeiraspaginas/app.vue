<template>
  <div
    class="tw-flex tw-h-screen tw-items-center tw-justify-center tw-bg-gray-300"
  >
    <div>
      <div class="tw-grid tw-grid-cols-12">
        <div class="tw-w-96 tw-col-start-6">
          <h1 class="tw-font-bold tw-font-mono tw-text-center tw-text-xl">
            Interpretador
          </h1>
          <div
            class="tw-bg-white tw-m-6 tw-shadow-2xl tw-p-6 tw-rounded-md tw-space-y-2"
          >
            <div>
              <input
                v-model="code"
                type="text"
                class="tw-w-full tw-bg-gray-50 tw-border tw-border-gray-400 tw-p-1 tw-rounded-md"
              />
            </div>
            <button
              @click="interpret(code)"
              class="tw-w-full tw-py-2 tw-rounded-md tw-bg-blue-600 tw-text-white tw-hover:bg-blue-800"
            >
              Interpretar
            </button>
          </div>
        </div>
      </div>
      <div class="tw-grid-cols-12 tw-grid tw-grid-flow-col">
        <div
          class="tw-bg-gray-100 tw-m-6 tw-shadow-2xl tw-p-6 tw-col-span-6 tw-rounded-md"
        >
          <div class="tw-font-bold tw-font-mono tw-text-center tw-text-xl">
            Lexer
          </div>
          <div class="tw-bg-gray-50 tw-border tw-border-gray-400 tw-rounded-md">
            <div class="tw-p-4">
              Minim ullamco mollit fugiat occaecat cillum nostrud excepteur
              velit sit sit. Anim qui sint quis ad fugiat. Proident cupidatat
              laborum amet qui enim est nisi ex occaecat ea irure cupidatat.
            </div>
          </div>
        </div>

        <div
          class="tw-bg-gray-100 tw-m-6 tw-shadow-2xl tw-p-6 tw-col-span-6 tw-rounded-md"
        >
          <div class="tw-font-bold tw-font-mono tw-text-center tw-text-xl">
            Parser
          </div>
          <div class="tw-bg-gray-50 tw-border tw-border-gray-400 tw-rounded-md">
            <div class="tw-p-4">
              Minim ullamco mollit fugiat occaecat cillum nostrud excepteur
              velit sit sit. Anim qui sint quis ad fugiat. Proident cupidatat
              laborum amet qui enim est nisi ex occaecat ea irure cupidatat.
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "App",
  data: () => ({
    code: "",
  }),
  methods: {
    extractLink(code) {
      const regex = /(https?:\/\/[^\s]+)/g;
      const match = code.match(regex);
      if (match) {
        return match[0];
      } else {
        return "";
      }
    },
    interpret(code) {
      // Enviar o código como JSON para o servidor Flask
      fetch('http://localhost:5000/analyze', {  // Certifique-se de que a URL corresponda ao seu servidor Flask
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ code }),
      })
        .then(response => response.json())
        .then(data => {
          // Atualizar a resposta com a resposta do servidor
          this.resposta = data.message;
          
        })
        .catch(error => {
          console.error('Erro ao analisar código:', error);
        });
    },
  },
};
</script>
