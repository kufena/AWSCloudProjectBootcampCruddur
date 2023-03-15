using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace SignupLambda {

    public class UserModel
    {
        public UserModel(string? em, string? cogid, string? display, string? handle) {
            this.email = em;
            this.cognito_user_id = cogid;
            this.display_name = display;
            this.handle = handle;
        }

        public UserModel(string uuid, string email, string cognito_user_id, string display_name, string handle)
        {
            this.uuid = uuid;    
            this.email = email;
            this.cognito_user_id = cognito_user_id;
            this.display_name = display_name;
            this.handle = handle;

        }

        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Computed)] // Identity or Computed?
        public string? uuid { get; set; }
        public string? email { get; set; }
        public string? cognito_user_id { get; set; }
        public string? display_name { get; set; }
        public string? handle { get; set; }
    }
}