import { Component, Input, SimpleChanges } from '@angular/core';
import { FormControl, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { ApiService } from '../../services/api.service';
import { Router } from '@angular/router';
import Swal from 'sweetalert2';
import { type_product } from '../../types/product';
import { NgIf } from '@angular/common';

@Component({
  selector: 'app-form-product',
  standalone: true,
  imports: [ReactiveFormsModule, NgIf],
  templateUrl: './form-product.component.html',
  styleUrl: './form-product.component.css'
})
export class FormProductComponent {
  @Input() formDataToEdit: type_product | null = null;

  productForm: FormGroup;

  constructor(private apiService: ApiService, private router: Router) {
    this.productForm = new FormGroup({
      'nome': new FormControl(null, [Validators.required]),
      'capa': new FormControl(null, [Validators.required, Validators.maxLength(125)]),
      'preco': new FormControl(null, [Validators.required]),
      'avaliacoes': new FormControl(null, [Validators.required]),
      'marca': new FormControl(null, [Validators.required]),
      'descricao': new FormControl(null, [Validators.required])

    })
  }

  ngOnChanges(changes: SimpleChanges) {
    if (changes["formDataToEdit"].currentValue != null) {
      console.log("foiii", this.formDataToEdit)
      this.setFormValues()
    }

  }
  setFormValues() {
    console.log("formDataToEdit", this.formDataToEdit)
    if (this.formDataToEdit !== null) {
      this.productForm.setValue(this.formDataToEdit);
      Object.keys(this.productForm.controls).forEach(controlName => {
        this.productForm.get(controlName)?.markAsTouched();
      });
    }

  }
  onSubmit(form: FormGroup) {
    if (this.formDataToEdit !== null) {
      this.apiService.editarProduto(this.formDataToEdit?._id!, form.value);
      this.rediracionaPrincipal()
    } else {
      this.apiService.addProduct(form.value).subscribe((res) => {
        Swal.fire({
          icon: 'success',
          title: 'Sucesso!',
          text: 'Produto adicionado com sucesso.',
          timer: 2500,
          showConfirmButton: false,
        });
        this.productForm.reset()
      })
    }

  }
  rediracionaPrincipal() {
    setTimeout(() => {
      this.router.navigate(['painel']);
    }, 2000);
  }
}
