document.addEventListener('DOMContentLoaded', () => {

  // --- LÓGICA DE LOGIN ---
  const formLogin = document.getElementById('formLogin');
  const btnTogglePass = document.getElementById('btnTogglePass');
  const passwordInput = document.getElementById('passwordInput');
  const eyeIcon = document.getElementById('eyeIcon');

  if (btnTogglePass && passwordInput) {
    btnTogglePass.addEventListener('click', () => {
      const isPassword = passwordInput.type === 'password';
      passwordInput.type = isPassword ? 'text' : 'password';
      eyeIcon.className = isPassword ? 'bi bi-eye-slash' : 'bi bi-eye';
    });
  }

  if (formLogin) {
    formLogin.addEventListener('submit', (e) => {
      e.preventDefault();
      // Redireciona para o Dashboard
      window.location.href = 'index-mobile.html';
    });
  }

  // --- LÓGICA DO DASHBOARD ---
  const btnToggleSidebar = document.getElementById('btnToggleSidebar');
  const mainSidebar = document.getElementById('mainSidebar');
  const sidebarBackdrop = document.getElementById('sidebarBackdrop');

  function toggleMobileMenu() {
    if (mainSidebar && sidebarBackdrop) {
      mainSidebar.classList.toggle('open');
      sidebarBackdrop.classList.toggle('active');
    }
  }

  if (btnToggleSidebar) btnToggleSidebar.addEventListener('click', toggleMobileMenu);
  if (sidebarBackdrop) sidebarBackdrop.addEventListener('click', toggleMobileMenu);

  // Alternar Menu Ativo na Sidebar
  const menuItems = document.querySelectorAll('.menu-item');
  menuItems.forEach(item => {
    item.addEventListener('click', (e) => {
      e.preventDefault();
      menuItems.forEach(i => i.classList.remove('active'));
      item.classList.add('active');
    });
  });

  // Switcher de Tema
  const btnThemeLight = document.getElementById('btnThemeLight');
  const btnThemeDark = document.getElementById('btnThemeDark');

  if (btnThemeLight && btnThemeDark) {
    btnThemeLight.addEventListener('click', () => {
      document.body.classList.remove('dark-mode');
      btnThemeLight.classList.add('active');
      btnThemeDark.classList.remove('active');
    });

    btnThemeDark.addEventListener('click', () => {
      document.body.classList.add('dark-mode');
      btnThemeDark.classList.add('active');
      btnThemeLight.classList.remove('active');
    });
  }

  // Filtro de Período Simulado
  const periodFilter = document.getElementById('periodFilter');
  const currentDateLabel = document.getElementById('currentDateLabel');

  if (periodFilter && currentDateLabel) {
    periodFilter.addEventListener('change', (e) => {
      const val = e.target.value;
      if (val === 'hoje') currentDateLabel.textContent = '(22/09/2026)';
      if (val === 'amanha') currentDateLabel.textContent = '(23/09/2026)';
      if (val === 'semana') currentDateLabel.textContent = '(20/09 a 26/09)';
    });
  }

  // Clique no perfil
  const userProfileBtn = document.getElementById('userProfileBtn');
  if (userProfileBtn) {
    userProfileBtn.addEventListener('click', () => {
      alert('Menu do Perfil da Camille Oliveira');
    });
  }

});

// --- LÓGICA DA TELA DE NOVA VISITA (Atualização Dinâmica do Resumo) ---
  const selectCliente = document.getElementById('selectCliente');
  const selectTecnico = document.getElementById('selectTecnico');
  const inputData = document.getElementById('inputData');
  const inputHorario = document.getElementById('inputHorario');

  const previewCliente = document.getElementById('previewCliente');
  const previewTecnico = document.getElementById('previewTecnico');
  const previewDataHora = document.getElementById('previewDataHora');
  const formNovaVisita = document.getElementById('formNovaVisita');

  document.addEventListener('DOMContentLoaded', () => {

  // Captura o formulário de Nova Visita
  const formNovaVisita = document.getElementById('formNovaVisita');

  if (formNovaVisita) {
    formNovaVisita.addEventListener('submit', function (event) {
      event.preventDefault(); // Impede o recarregamento padrão da página

      // Captura o campo de texto do cliente
      const inputCliente = document.getElementById('clienteNome');

      if (!inputCliente || !inputCliente.value.trim()) {
        alert('Por favor, preencha o nome do cliente / visitante.');
        return;
      }

      const nomeDigitado = inputCliente.value.trim();

      // Sucesso
      alert('Visita agendada com sucesso para: ' + nomeDigitado);

      // Redireciona para o Dashboard (index-mobile.html)
      window.location.href = 'index-mobile.html';
    });
  }

});

  // Atualizar técnico no resumo
  if (selectTecnico && previewTecnico) {
    selectTecnico.addEventListener('change', (e) => {
      previewTecnico.textContent = e.target.value;
      previewTecnico.classList.remove('muted');
    });
  }

  // Atualizar data/hora no resumo
  function updateDataHora() {
    if (inputData && inputHorario && previewDataHora) {
      let dataVal = inputData.value; //AAAA-MM-DD
      if (dataVal) {
        const partes = dataVal.split('-');
        dataVal = `${partes[2]}/${partes[1]}/${partes[0]}`;
      } else {
        dataVal = '26/09/2026';
      }
      const horaVal = inputHorario.value || '08:00';
      previewDataHora.textContent = `${dataVal} - ${horaVal}`;
    }
  }

  if (inputData) inputData.addEventListener('change', updateDataHora);
  if (inputHorario) inputHorario.addEventListener('change', updateDataHora);

  // Submeter formulário
  if (formNovaVisita) {
    formNovaVisita.addEventListener('submit', (e) => {
      e.preventDefault();
      alert('Visita agendada com sucesso!');
      window.location.href = 'index-mobile.html'; // Redireciona para o dashboard
    });
  }

  // --- LÓGICA DE DETALHES DA VISITA (Carregamento Dinâmico de Parâmetros da URL) ---
  const urlParams = new URLSearchParams(window.location.search);
  const clienteParam = urlParams.get('cliente');
  const tecnicoParam = urlParams.get('tecnico');
  const enderecoParam = urlParams.get('endereco');

  if (clienteParam) {
    const visitClientLabel = document.getElementById('visitClientLabel');
    if (visitClientLabel) visitClientLabel.textContent = clienteParam;
  }

  if (tecnicoParam) {
    const visitTechLabel = document.getElementById('visitTechLabel');
    if (visitTechLabel) visitTechLabel.textContent = tecnicoParam;
  }

  if (enderecoParam) {
    const visitAddressLabel = document.getElementById('visitAddressLabel');
    if (visitAddressLabel) visitAddressLabel.textContent = `Endereço: ${enderecoParam}`;
  }

  // --- LÓGICA DO MODAL DE ADICIONAR PARTICIPANTE ---
  const modalAddParticipant = document.getElementById('modalAddParticipant');
  const btnOpenAddParticipant = document.getElementById('btnOpenAddParticipant');
  const btnCloseParticipantModal = document.getElementById('btnCloseParticipantModal');
  const btnCancelModal = document.getElementById('btnCancelModal');
  const formAddParticipant = document.getElementById('formAddParticipant');

  function openModal() {
    if (modalAddParticipant) modalAddParticipant.classList.add('active');
  }

  function closeModal() {
    if (modalAddParticipant) modalAddParticipant.classList.remove('active');
  }

  if (btnOpenAddParticipant) btnOpenAddParticipant.addEventListener('click', openModal);
  if (btnCloseParticipantModal) btnCloseParticipantModal.addEventListener('click', closeModal);
  if (btnCancelModal) btnCancelModal.addEventListener('click', closeModal);

  if (formAddParticipant) {
    formAddParticipant.addEventListener('submit', (e) => {
      e.preventDefault();
      alert('Participante adicionado com sucesso!');
      closeModal();
    });
  }

  document.addEventListener('DOMContentLoaded', () => {

  const formNovaVisita = document.getElementById('formNovaVisita');

  if (formNovaVisita) {
    formNovaVisita.addEventListener('submit', function (event) {
      event.preventDefault();

      // Captura os campos
      const inputCliente = document.getElementById('clienteNome');
      const inputTurma = document.getElementById('turmaNome');

      // Validação do Cliente
      if (!inputCliente || !inputCliente.value.trim()) {
        alert('Por favor, preencha o nome do cliente / visitante.');
        return;
      }

      // Validação da Turma
      if (!inputTurma || !inputTurma.value.trim()) {
        alert('Por favor, informe a turma.');
        return;
      }

      const nomeDigitado = inputCliente.value.trim();
      const turmaDigitada = inputTurma.value.trim();

      console.log('Dados do agendamento:', {
        cliente: nomeDigitado,
        turma: turmaDigitada
      });

      // Feedback visual e redirecionamento
      alert(`Visita agendada com sucesso!\nCliente: ${nomeDigitado}\nTurma: ${turmaDigitada}`);
      window.location.href = 'index-mobile.html';
    });
  }

});

document.addEventListener('DOMContentLoaded', () => {

  // --- LÓGICA DA PÁGINA DETALHES DA VISITA (Editar e Cancelar) ---
  const btnEditVisit = document.getElementById('btnEditVisit');
  const btnCancelVisit = document.getElementById('btnCancelVisit');
  const modalCancelVisit = document.getElementById('modalCancelVisit');
  const btnCloseCancelModal = document.getElementById('btnCloseCancelModal');
  const btnKeepVisit = document.getElementById('btnKeepVisit');
  const btnConfirmCancel = document.getElementById('btnConfirmCancel');

  // 1. AÇÃO DE EDITAR VISITA
  if (btnEditVisit) {
    btnEditVisit.addEventListener('click', () => {
      // Pega os dados exibidos atualmente na tela
      const cliente = document.getElementById('visitClientLabel')?.textContent || '';
      const endereco = document.getElementById('visitAddressLabel')?.textContent.replace('Endereço: ', '') || '';

      // Redireciona para a página de nova visita/edição passando os dados pela URL
      window.location.href = `nova-visita-mobile.html?modo=editar&cliente=${encodeURIComponent(cliente)}&endereco=${encodeURIComponent(endereco)}`;
    });
  }

  // 2. AÇÃO DE CANCELAR VISITA (Abertura e Fechamento do Modal)
  function openCancelModal() {
    if (modalCancelVisit) modalCancelVisit.classList.add('active');
  }

  function closeCancelModal() {
    if (modalCancelVisit) modalCancelVisit.classList.remove('active');
  }

  if (btnCancelVisit) btnCancelVisit.addEventListener('click', openCancelModal);
  if (btnCloseCancelModal) btnCloseCancelModal.addEventListener('click', closeCancelModal);
  if (btnKeepVisit) btnKeepVisit.addEventListener('click', closeCancelModal);

  // Confirmação do Cancelamento
  if (btnConfirmCancel) {
    btnConfirmCancel.addEventListener('click', () => {
      // Atualiza as tags de status visualmente na página
      const statusTags = document.querySelectorAll('#mainStatusTag, .detail-header-title .tag');
      
      statusTags.forEach(tag => {
        tag.textContent = 'Cancelada';
        tag.className = 'tag tag-red'; // Aplica a cor vermelha de cancelado
      });

      closeCancelModal();
      alert('A visita foi cancelada com sucesso!');
    });
  }

});

// --- LÓGICA DE PESQUISA E FILTRO DA TABELA DE VISITAS ---
  const inputSearchVisits = document.getElementById('inputSearchVisits');
  const selectStatusFilter = document.getElementById('selectStatusFilter');
  const visitsTable = document.getElementById('visitsTable');

  function filterVisitsTable() {
    if (!visitsTable) return;

    const searchTerm = inputSearchVisits ? inputSearchVisits.value.toLowerCase().trim() : '';
    const selectedStatus = selectStatusFilter ? selectStatusFilter.value : 'todos';
    
    const rows = visitsTable.querySelectorAll('tbody tr');
    let visibleCount = 0;

    rows.forEach(row => {
      const textRow = row.textContent.toLowerCase();
      const statusTag = row.querySelector('.tag') ? row.querySelector('.tag').textContent.trim() : '';

      const matchesSearch = textRow.includes(searchTerm);
      const matchesStatus = (selectedStatus === 'todos') || (statusTag === selectedStatus);

      if (matchesSearch && matchesStatus) {
        row.style.display = '';
        visibleCount++;
      } else {
        row.style.display = 'none';
      }
    });

    // Atualiza contador no rodapé se existir
    const paginationSummary = document.getElementById('paginationSummary');
    if (paginationSummary) {
      paginationSummary.textContent = `Mostrando ${visibleCount} visita(s) encontrada(s)`;
    }
  }

  // Eventos de digitação e mudança de filtro
  if (inputSearchVisits) {
    inputSearchVisits.addEventListener('input', filterVisitsTable);
  }

  if (selectStatusFilter) {
    selectStatusFilter.addEventListener('change', filterVisitsTable);
  }