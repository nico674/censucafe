    // Recibimos los datos desde el contexto de Django
    const etiquetas = JSON.parse('{{ etiquetas|escapejs }}');
    const valores = JSON.parse('{{ valores|escapejs }}');
    const radarLabels = JSON.parse('{{ radar_labels|escapejs }}');
    const radarData = JSON.parse('{{ radar_data|escapejs }}');
    const pieLabels = JSON.parse('{{ pie_labels|escapejs }}');
    const pieData = JSON.parse('{{ pie_data|escapejs }}');

    // Gráfico de Líneas
    new Chart(document.getElementById('lineChart'), {
      type: 'line',
      data: {
        labels: etiquetas,
        datasets: [{
          label: 'Ventas',
          data: valores,
          borderColor: 'blue',
          backgroundColor: 'rgba(0,0,255,0.2)',
          tension: 0.4
        }]
      }
    });

    // Gráfico de Barras
    new Chart(document.getElementById('barChart'), {
      type: 'bar',
      data: {
        labels: etiquetas,
        datasets: [{
          label: 'Ventas',
          data: valores,
          backgroundColor: 'orange',
        }]
      }
    });

    // Gráfico de Radar
    new Chart(document.getElementById('radarChart'), {
      type: 'radar',
      data: {
        labels: radarLabels,
        datasets: [{
          label: 'Perfil Sensorial',
          data: radarData,
          backgroundColor: 'rgba(54, 162, 235, 0.2)',
          borderColor: 'rgb(54, 162, 235)',
          pointBackgroundColor: 'rgb(54, 162, 235)'
        }]
      }
    });

    // Gráfico de Pie
    new Chart(document.getElementById('pieChart'), {
      type: 'pie',
      data: {
        labels: pieLabels,
        datasets: [{
          label: 'Evaluaciones',
          data: pieData,
          backgroundColor: ['green', 'yellow', 'red']
        }]
      }
    });