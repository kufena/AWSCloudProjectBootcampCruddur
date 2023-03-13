using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace SignupLambda {

    public class UserModel
    {
        public UserModel(string? em, string? cogid, string? display, string? handle) {
            this.email = em;
            this.user_cognito_id = cogid;
            this.display_name = display;
            this.handle = handle;
        }

        public UserModel(string uuid, string em, string cogid, string display, string handle)
        {
            this.uuid = uuid;    
            this.email = em;
            this.user_cognito_id = cogid;
            this.display_name = display;
            this.handle = handle;

        }

        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.None)]
        public string? uuid { get; set; }
        public string? email { get; set; }
        public string? user_cognito_id { get; set; }
        public string? display_name { get; set; }
        public string? handle { get; set; }
    }
}