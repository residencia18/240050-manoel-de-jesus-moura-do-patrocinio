import { Component, ElementRef, ViewChild } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { ApiService } from '../../services/api.service';
import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import Swal from 'sweetalert2';
import { NgFor, NgIf } from '@angular/common';
import { type_suino_peso } from '../../types/type_suino';
import { LineChartComponent } from '../../components/line-chart/line-chart.component';
import { FormatdatePipe } from '../../pipes/formatdate.pipe';

@Component({
  selector: 'app-register-peso',
  standalone: true,
  imports: [ReactiveFormsModule, NgIf, NgFor, RouterLink, LineChartComponent, FormatdatePipe],
  templateUrl: './register-peso.component.html',
  styleUrl: './register-peso.component.css'
})
export class RegisterPesoComponent {
  SuinoPesoForm: FormGroup = new FormGroup({});
  suinoId: string = ""
  suinopesoHistorico: type_suino_peso[] = []

  pesos: number[] = [];
  datas: string[] = []





  constructor(private apiService: ApiService, private formBuilder: FormBuilder, private rotas: Router, private rota: ActivatedRoute) { }

  ngOnInit(): void {
    this.suinoId = this.rota.snapshot.params['id']
    this.SuinoPesoForm = this.formBuilder.group({
      'DataPesagem': [null, [Validators.required]],
      'suinoPeso': [null, [Validators.required]],
    })

    this.apiService.getListPesoSuinos().subscribe((response) => {
      this.suinopesoHistorico = response.filter((suino) => suino.suinoBrinco == this.suinoId)
      if (this.suinopesoHistorico.length > 0) {
        this.formatDatasToChart(this.suinopesoHistorico)
      }
    })

  }


  formatDatasToChart(data: type_suino_peso[]) {
    //  Transforma a data do formato "yyyy-mm-dd" para o padrão Date()
    data.forEach(peso => {
      peso.DataPesagem = new Date(peso.DataPesagem);
    });
    // ordena as dados por ordem crescente
    data.sort((a, b) => a.DataPesagem.getTime() - b.DataPesagem.getTime());

    this.pesos = data.map(suino => suino.suinoPeso)
    this.datas = data.map(suino => suino.DataPesagem.toLocaleDateString())

  }

  onSubmit(form: FormGroup) {
    if (this.SuinoPesoForm.valid) {

      const DataPeso = {
        ...form.value,
        suinoBrinco: this.suinoId
      }
      this.apiService.cadastroPesoSuino(DataPeso).subscribe(responseData => {
        Swal.fire({
          icon: 'success',
          title: 'Sucesso!',
          text: 'Peso adicionado com sucesso.',
          timer: 2000,
          showConfirmButton: false,
        });
        setTimeout(() => {
          this.SuinoPesoForm.reset()
          window.location.reload();

        }, 2500)
      });
    }

  }
}
