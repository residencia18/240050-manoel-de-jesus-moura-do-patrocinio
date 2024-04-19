import { Component, Input, SimpleChanges } from '@angular/core';
import Chart from 'chart.js/auto';

@Component({
  selector: 'app-line-chart',
  standalone: true,
  imports: [],
  templateUrl: './line-chart.component.html',
  styleUrl: './line-chart.component.css'
})
export class LineChartComponent {
  chart: any = []
  @Input() pesos: number[] = []
  @Input() datas: string[] = []


  ngOnChanges(changes: SimpleChanges) {


    if (changes["datas"].currentValue.length > 0|| changes["pesos"].currentValue.length > 0) {
      this.createChart();
    }

  }

  createChart() {

    this.chart = new Chart('canvas', {
      type: 'line',
      data: {
        labels: this.datas,
        datasets: [
          {
            label: 'Peso',
            data: this.pesos,
            borderWidth: 1,
          },
        ],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
          },
        },
      },
    });


  }
}
