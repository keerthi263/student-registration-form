<script>
import { onMount } from 'svelte'

let students = []

let form = {
  id: null,
  name: '',
  email: '',
  course: ''
}

const API_URL = 'http://127.0.0.1:5000/students'

async function fetchStudents() {
  const response = await fetch(API_URL)
  students = await response.json()
}

async function saveStudent() {
  if (form.id) {
    await fetch(`${API_URL}/${form.id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form)
    })
  } else {
    await fetch(API_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form)
    })
  }

  resetForm()
  fetchStudents()
}

function editStudent(student) {
  form = { ...student }
}

async function removeStudent(id) {
  await fetch(`${API_URL}/${id}`, {
    method: 'DELETE'
  })

  fetchStudents()
}

function resetForm() {
  form = {
    id: null,
    name: '',
    email: '',
    course: ''
  }
}

onMount(fetchStudents)
</script>

<div class="container">
  <h1>Student Registration CRUD App</h1>

  <form on:submit|preventDefault={saveStudent}>
    <input bind:value={form.name} placeholder="Name" required />
    <br>
    <br>
    <input bind:value={form.email} type="email" placeholder="Email" required />
    <br>

    <br>
    <input bind:value={form.course} placeholder="Course" required />
    <br>
    <br>
    <button type="submit">
      {form.id ? 'Update' : 'Add'}
    </button>
  </form>

  <table>
    <thead>
      <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Email</th>
        <th>Course</th>
        <th>Actions</th>
      </tr>
    </thead>

    <tbody>
      {#each students as student}
      <tr>
        <td>{student.id}</td>
        <td>{student.name}</td>
        <td>{student.email}</td>
        <td>{student.course}</td>
        <td>
          <button on:click={() => editStudent(student)}>Edit</button>
          <button on:click={() => removeStudent(student.id)}>Delete</button>
        </td>
      </tr>
      {/each}
    </tbody>
  </table>
</div>

<style>
</style>
