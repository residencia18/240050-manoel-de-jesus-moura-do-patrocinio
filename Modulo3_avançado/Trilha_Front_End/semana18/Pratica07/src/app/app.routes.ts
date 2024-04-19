import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { ListagemSuinosComponent } from './pages/listagem-suinos/listagem-suinos.component';
import { LoginComponent } from './pages/login/login.component';
import { CadastroUsuarioComponent } from './pages/cadastro-usuario/cadastro-usuario.component';
import { EdicaoSuinoComponent } from './pages/edicao-suino/edicao-suino.component';
import { RegisterPesoComponent } from './pages/register-peso/register-peso.component';
import { EditPesoComponent } from './pages/edit-peso/edit-peso.component';
import { AuthGuard,canActivateGuard } from './auth-guard.guard';
import { RegisterManejoComponent } from './pages/register-manejo/register-manejo.component';
import { ListManejoComponent } from './pages/list-manejo/list-manejo.component';
import { ManegerManejoComponent } from './pages/maneger-manejo/maneger-manejo.component';


export const routes: Routes = [
    {path:"", component: HomeComponent},
    {path:"register-suino", loadComponent: ()=> import('./pages/cadastro-suinos/cadastro-suinos.component').then((c) => c.CadastroSuinosComponent) },
    {path:"list-suino", loadComponent: ()=> import('./pages/listagem-suinos/listagem-suinos.component').then((c) => c.ListagemSuinosComponent) },
    {path:"edit-suino/:id", loadComponent: ()=> import('./pages/edicao-suino/edicao-suino.component').then((c) => c.EdicaoSuinoComponent) },

    {path:"register-peso/:id", loadComponent: ()=> import('./pages/register-peso/register-peso.component').then((c) => c.RegisterPesoComponent) },
    {path:"edit-peso/:id", loadComponent: ()=> import('./pages/edit-peso/edit-peso.component').then((c) => c.EditPesoComponent) },

    {path:"login", loadComponent: ()=> import('./pages/login/login.component').then((c) => c.LoginComponent) },
    {path:"register", loadComponent: ()=> import('./pages/cadastro-usuario/cadastro-usuario.component').then((c) => c.CadastroUsuarioComponent) },

    {path:"register-manejo", loadComponent: ()=> import('./pages/register-manejo/register-manejo.component').then((c) => c.RegisterManejoComponent) },
    {path:"list-manejo", loadComponent: ()=> import('./pages/list-manejo/list-manejo.component').then((c) => c.ListManejoComponent) },
    {path:"menage-manejo/:id", loadComponent: ()=> import('./pages/maneger-manejo/maneger-manejo.component').then((c) => c.ManegerManejoComponent) },


];
